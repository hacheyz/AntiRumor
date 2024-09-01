package cn.edu.hit.backend.service.impl;

import cn.edu.hit.backend.mapper.TagMapper;
import cn.edu.hit.backend.pojo.PageBean;
import cn.edu.hit.backend.pojo.Tag;
import cn.edu.hit.backend.service.TagService;
import com.github.pagehelper.Page;
import com.github.pagehelper.PageHelper;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Map;

@Service
public class TagServiceImpl implements TagService {

  @Autowired
  private TagMapper tagMapper;

  @Override
  public Tag findByTagName(String name) {
    return tagMapper.findByTagName(name);
  }

  @Override
  public void addTag(String name) {
    tagMapper.add(name);
  }

  // 分页查询
  @Override
  public PageBean<Tag> pagelist(Map<String, Object> map) {
    // 1. 创建PageBean对象
    PageBean<Tag> pb = new PageBean<>();
    Integer pageNum = (Integer) map.get("pageNum");
    Integer pageSize = (Integer) map.get("pageSize");

    // 2. 开启分页查询 PageHelper
    PageHelper.startPage(pageNum, pageSize);

    // 3. 调用mapper
    List<Tag> as = tagMapper.list();
    //Page中提供了方法,可以获取PageHelper分页查询后 得到的总记录条数和当前页数据
    Page<Tag> p = (Page<Tag>) as;

    //把数据填充到PageBean对象中
    pb.setTotal(p.getTotal());
    pb.setItems(p.getResult());

    return pb;
  }

  // 返回标签列表（不带关联rumor条数）
  @Override
  public List<Tag> list() {
    return tagMapper.list();
  }

  // 返回标签列表（带关联rumor条数）
  @Override
  public List<Tag> listWithRelateNum() {
    List<Tag> tagList = tagMapper.list();
    for(Tag tag : tagList) {
      Integer tagId = tag.getId();
      tag.setRelateNum(tagMapper.getRelateNumByTagId(tagId));
    }
    return tagList;
  }
}
