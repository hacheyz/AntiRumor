package cn.edu.hit.backend.mapper;

import cn.edu.hit.backend.pojo.Rumor;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Map;

@Mapper
public interface RumorMapper {
  @Select("select * from rumor")
  List<Rumor> list();
}
