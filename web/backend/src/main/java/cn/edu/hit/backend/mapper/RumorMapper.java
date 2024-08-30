package cn.edu.hit.backend.mapper;

import cn.edu.hit.backend.pojo.Rumor;
import cn.edu.hit.backend.pojo.Tag;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Param;
import org.apache.ibatis.annotations.Select;

import java.util.List;
import java.util.Map;

@Mapper
public interface RumorMapper {

//  @Select("select * from rumor")
  List<Rumor> pagelist(@Param("searchRumor") String searchRumor,
                       @Param("searchTags") List<String> searchTags,
                       @Param("searchTagListLength") Integer searchTagListLength);

  @Select("SELECT t.* FROM tag t " +
      "INNER JOIN rumor_tag rt ON t.id = rt.tag_id " +
      "WHERE rt.rumor_id = #{rumorId}")
  List<Tag> getTagsForRumor(Integer rumorId);
}
